def calculate_molarity():
    try:
        print("몰농도 계산기")
        print("1. 몰농도 구하기")
        print("2. 용질의 양 구하기")
        print("3. 화학식 계산기")
        print("4. 종료")
        choice = input("원하는 작업을 선택하세요 (1 또는 2 또는 3 또는 4): ")

        if choice == '1':
            n = float(input("용질의 몰 수 (mol)를 입력하세요: "))
            V = float(input("용액의 부피 (L)를 입력하세요: "))
            C = n / V
            print(f"몰농도는 {C:.2f} mol/L 입니다.")

        elif choice == '2':
            m= float(input("몰농도의 양(mol/L)를 입력하세요:"))
            V = float(input("용액의 부피 (L)를 입력하세요: "))
            C = m*V
            print(f"용질의 양은 {C: .2f} mol 입니다.")

        elif choice == '4':
            print("프로그램을 종료합니다.")

        elif choice =='3':
            from collections import defaultdict


            atomic_weights = {
                'H': 1.008,
                'He': 4.0026,
                'Li': 6.94,
                'Be': 9.0122,
                'B': 10.81,
                'C': 12.011,
                'N': 14.007,
                'O': 15.999,
                'F': 18.998,
                'Ne': 20.180,
                'Na': 22.990,
                'Mg': 24.305,
                'Al': 26.982,
                'Si': 28.085,
                'P': 30.974,
                'S': 32.06,
                'Cl': 35.45,
                'Ar': 39.948,
                'K': 39.098,
                'Ca': 40.078,
                'Sc': 44.956,
                'Ti': 47.867,
                'V': 50.941,
                'Cr': 51.996,
                'Mn': 54.938,
                'Fe': 55.845,
                'Co': 58.933,
                'Ni': 58.693,
                'Cu': 63.546,
                'Zn': 65.38,
                'Ga': 69.723,
                'Ge': 72.630,
                'As': 74.922,
                'Se': 78.971,
                'Br': 79.904,
                'Kr': 83.798,
                'Rb': 85.468,
                'Sr': 87.62,
                'Y': 88.906,
                'Zr': 91.224,
                'Nb': 92.906,
                'Mo': 95.95,
                'Tc': 98,
                'Ru': 101.07,
                'Rh': 102.91,
                'Pd': 106.42,
                'Ag': 107.87,
                'Cd': 112.41,
                'In': 114.82,
                'Sn': 118.71,
                'Sb': 121.76,
                'Te': 127.60,
                'I': 126.90,
                'Xe': 131.29,
                'Cs': 132.91,
                'Ba': 137.33,
                'La': 138.91,
                'Ce': 140.12,
                'Pr': 140.91,
                'Nd': 144.24,
                'Sm': 150.36,
                'Eu': 151.96,
                'Gd': 157.25,
                'Dy': 162.50,
                'Ho': 164.93,
                'Er': 167.26,
                'Tm': 168.93,
                'Yb': 173.04,
                'Lu': 174.97,
                'Hf': 178.49,
                'Ta': 180.95,
                'W': 183.84,
                'Re': 186.21,
                'Os': 190.23,
                'Ir': 192.22,
                'Pt': 195.08,
                'Au': 196.97,
                'Hg': 200.59,
                'Tl': 204.38,
                'Pb': 207.2,
                'Bi': 208.98,
                'Po': 209,
                'At': 210,
                'Rn': 222,
            }
            def calculate_molecular_weight(formula):
                    element_counts = defaultdict(int)
                    i = 0
                    n = len(formula)
                    
                    while i < n:
                        if formula[i].isalpha():
                            element = formula[i]
                            if i + 1 < n and formula[i + 1].islower():
                                element += formula[i + 1]
                                i += 1
                            count = 1
                            if i + 1 < n and formula[i + 1].isdigit():
                                count_str = ''
                                while i + 1 < n and formula[i + 1].isdigit():
                                    count_str += formula[i + 1]
                                    i += 1
                                count = int(count_str)
                            element_counts[element] += count
                        i += 1

                    total_weight = 0.0
                    for element, count in element_counts.items():
                        if element in atomic_weights:
                            total_weight += atomic_weights[element] * count
                        else:
                            print(f"경고: 원소 {element}의 원자량을 찾을 수 없습니다.")
                    
                    return total_weight

            # 사용자 입력 받기
            chemical_formula = input("화학식을 입력하세요: ")
            mass = float(input("질량(g)을 입력하세요: "))

            molecular_weight = calculate_molecular_weight(chemical_formula)
            moles = mass / molecular_weight if molecular_weight > 0 else 0

            print(f"{chemical_formula}의 화학식량은 {molecular_weight:.2f} g/mol입니다.")
            print(f"입력한 질량 {mass} g에 해당하는 몰수는 {moles:.4f} mol입니다.")

        else:
            print("유효한 선택지를 입력하세요.")
                
    except ValueError:
        print("유효한 숫자를 입력하세요.")


# 함수 실행
calculate_molarity()
