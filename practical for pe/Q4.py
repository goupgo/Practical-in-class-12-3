from datetime import datetime

def read_temperature_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return lines

def calculate_average_daily_temperature(temperature_data):
    total_temperature = 0
    total_measurements = 0
    for i in range(0, len(temperature_data), 2):
        temperature = float(temperature_data[i+1])
        total_temperature += temperature
        total_measurements += 1
    if total_measurements == 0:
        return 0
    return total_temperature / total_measurements

def calculate_average_temperature_in_range(temperature_data, start_hour, end_hour):
    total_temperature = 0
    total_measurements = 0
    for i in range(0, len(temperature_data), 2):
        measurement_time = datetime.strptime(temperature_data[i].strip(), "%d-%m-%Y %H:%M:%S")
        temperature = float(temperature_data[i+1])
        if start_hour <= measurement_time.hour <= end_hour:
            total_temperature += temperature
            total_measurements += 1
    if total_measurements == 0:
        return 0
    return total_temperature / total_measurements

def main():
    file_path = "temp.txt"
    temperature_data = read_temperature_data(file_path)
    
    average_daily_temperature = calculate_average_daily_temperature(temperature_data)
    print("Average daily temperature:", round(average_daily_temperature, 3))

    average_temperature_5_to_15 = calculate_average_temperature_in_range(temperature_data, 5, 15)
    print("Average temperature from 5:00 to 15:59:", round(average_temperature_5_to_15, 3))

    average_temperature_16_to_21 = calculate_average_temperature_in_range(temperature_data, 16, 21)
    print("Average temperature from 16:00 to 21:59:", round(average_temperature_16_to_21, 3))

if __name__ == "__main__":
    main()
