import os

# ================= 配置区域 =================
INPUT_FILE = 'playdata.txt'  # 原始数据文件
OUTPUT_FILE = 'Warningdata.txt'  # 生成的新文件
DURATION_SEC = 30  # 生成总时长（秒）
LINES_PER_SEC = 500  # 原始数据的采样率（约110行/秒）
INJECT_INTERVAL = 250  # 每隔多少行插入一次数值包（约0.5秒刷新一次数值）

# 定义测试阶段 (开始秒, 结束秒, 心率HR, 血氧SPO2)
PHASES = [
    (0, 15, 75, 98),  # 正常
    (15, 30, 150, 98),  # 高心率报警
    (30, 45, 40, 98),  # 低心率报警
    (45, 60, 75, 85),  # 低血氧报警
    (60, 90, 75, 98),  # 恢复正常
]


# ===========================================

def get_status_for_time(current_sec):
    """根据当前时间判断应该处于哪个报警阶段"""
    for start, end, hr, spo2 in PHASES:
        if start <= current_sec < end:
            return hr, spo2
    return 75, 98  # 默认值


def generate_packet_hr(hr_val):
    """生成心率数据包 [16, 4, High, Low, 0, 0, 0, 0]"""
    # 0x10=16(ECG), 0x04=HR
    return f"[16, 4, {hr_val >> 8}, {hr_val & 0xFF}, 0, 0, 0, 0]"


def generate_packet_spo2(spo2_val, pr_val):
    """生成血氧数据包 [19, 3, 0, PR_H, PR_L, SPO2, 0, 0]"""
    # 0x13=19(SPO2), 0x03=Value
    return f"[19, 3, 0, {pr_val >> 8}, {pr_val & 0xFF}, {spo2_val}, 0, 0]"


def main():
    if not os.path.exists(INPUT_FILE):
        print(f"错误：找不到 {INPUT_FILE}，请确保该文件在当前目录下。")
        return

    # 1. 读取原始数据，提取波形背景（剔除旧的心率/血氧数值包，避免冲突）
    waveform_lines = []
    with open(INPUT_FILE, 'r') as f:
        for line in f:
            line = line.strip()
            if not line: continue
            # 将字符串转为列表进行判断
            try:
                parts = eval(line)
                # 过滤掉 [16, 4, ...] 和 [19, 3, ...]
                if parts[0] == 16 and parts[1] == 4: continue
                if parts[0] == 19 and parts[1] == 3: continue
                waveform_lines.append(line)
            except:
                continue

    print(f"成功加载原始波形数据：{len(waveform_lines)} 行")

    # 2. 生成新文件
    total_lines_target = DURATION_SEC * LINES_PER_SEC
    output_lines = []

    print(f"开始生成 {DURATION_SEC} 秒的数据，预计 {total_lines_target} 行...")

    for i in range(total_lines_target):
        # A. 循环填充波形数据
        wave_line = waveform_lines[i % len(waveform_lines)]
        output_lines.append(wave_line)

        # B. 定期插入数值包 (保证报警响应速度)
        if i % INJECT_INTERVAL == 0:
            current_sec = i / LINES_PER_SEC
            target_hr, target_spo2 = get_status_for_time(current_sec)

            # 插入心率包
            output_lines.append(generate_packet_hr(target_hr))
            # 插入血氧包 (脉率通常跟随心率)
            output_lines.append(generate_packet_spo2(target_spo2, target_hr))

    # 3. 写入文件
    with open(OUTPUT_FILE, 'w') as f:
        for line in output_lines:
            f.write(line + "\n")

    print(f"生成完毕！文件已保存为: {OUTPUT_FILE}")
    print(f"总行数: {len(output_lines)}")
    print("请在软件的'演示模式'中加载此文件进行测试。")


if __name__ == '__main__':
    main()