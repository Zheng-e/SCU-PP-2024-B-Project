# health.py
def read_health_data(file_path):
    health_data = {}
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                parts = line.split(':')
                bmi_range = parts[0].strip('<> ')
                description = parts[1].strip().strip('"')
                if '<' in parts[0]:
                    limit = float(parts[0].strip('<'))
                    health_data[('lt', limit)] = description
                elif '>' in parts[0]:
                    limit = float(parts[0].strip('>'))
                    health_data[('gt', limit)] = description
    return health_data

def calculate_bmi(weight, height):
    if height == 0:
        raise ValueError("Height cannot be zero.")
    return weight / (height ** 2)

def determine_health_index(bmi, health_data):
    for (op, limit), description in health_data.items():
        if op == 'lt' and bmi < limit:
            return description
        elif op == 'gt' and bmi > limit:
            return description
    return "未知"

if __name__ == "__main__":
    health_data = read_health_data('health.txt')
    try:
        weight = float(input("请输入体重(kg): "))
        height = float(input("请输入身高(m): "))
        bmi = calculate_bmi(weight, height)
        health_index = determine_health_index(bmi, health_data)
        print(f"BMI: {bmi:.2f}, 健康指数: {health_index}")
    except ValueError as e:
        print(f"输入错误: {e}")
