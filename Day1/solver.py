def get_data():
    with open('input_day1.txt', 'r') as f:
        data = f.read().split('\n')
        data = list(map(int, data[:-1])) # Remove the last row which is empty
        
    return data


def solve_q1(data):
    total = 0
    
    for i in range(len(data) - 1):
        if data[i] < data[i + 1]:
            total += 1
    
    print(total)

    
def solve_q2(data):
    total = 0
    
    for i in range(len(data) - 3):
        first_sum = data[i] + data[i + 1] + data[i + 2]
        second_sum = data[i +  1] + data[i + 2] + data[i + 3]
        if first_sum < second_sum:
            total += 1
            
    print(total)
    
if __name__ == '__main__':
    data = get_data()
    solve_q1(data)
    solve_q2(data)
