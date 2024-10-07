def calculateGrade(midterm1, midterm2, final):
    average = (midterm1 + midterm2 + final) / 3
    if average >= 90:
        return 'A'
    elif average >= 80:
        return 'B'
    elif average >= 70:
        return 'C'
    elif average >= 60:
        return 'D'
    return 'F'

def student_info(lines):
    report = []
    midterm1_total = midterm2_total = final_total = student_count = 0

    for line in lines:
        parts = line.strip().split('\t')
        last_name, first_name = parts[0], parts[1]
        midterm1, midterm2, final = map(int, parts[2:5])
        
        letter_grade = calculateGrade(midterm1, midterm2, final)
        report.append(f"{last_name}\t{first_name}\t{midterm1}\t{midterm2}\t{final}\t{letter_grade}")
        
        midterm1_total += midterm1
        midterm2_total += midterm2
        final_total += final
        student_count += 1

    return report, midterm1_total, midterm2_total, final_total, student_count

def make_report(report, midterm1_total, midterm2_total, final_total, student_count):
    avg_midterm1 = midterm1_total / student_count
    avg_midterm2 = midterm2_total / student_count
    avg_final = final_total / student_count

    with open('report.txt', 'w') as report_file:
        report_file.write('\n'.join(report) + '\n')
        report_file.write('\n')
        report_file.write(f"Averages: midterm1 {avg_midterm1:.2f}, midterm2 {avg_midterm2:.2f}, final {avg_final:.2f}" + '\n')

if __name__ == "__main__":
    filename = input()
    with open(filename, 'r') as file:
        lines = file.readlines()

    report, midterm1_total, midterm2_total, final_total, student_count = student_info(lines)
    make_report(report, midterm1_total, midterm2_total, final_total, student_count)