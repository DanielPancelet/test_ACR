class Matrix:
    def __init__(self, data):
        """Инициализация матрицы.
        
        Аргумент:
        data -- двумерный список (список списков), представляющий матрицу
        """
        if not data or not all(isinstance(row, list) for row in data):
            raise ValueError("Матрица должна быть двумерным списком.")
        self.data = data
        self.rows = len(data)
        self.cols = len(data[0])
        for row in data:
            if len(row) != self.cols:
                raise ValueError("Все строки матрицы должны иметь одинаковую длину.")

    def add(self, other):
        """Сложение двух матриц.
        
        Аргумент:
        other -- другая матрица (объект класса Matrix)
        
        Возвращает новую матрицу как результат сложения.
        """
        if self.rows != other.rows or self.cols != other.cols:
            raise ValueError("Матрицы должны быть одинакового размера для сложения.")
        result = []
        for i in range(self.rows):
            result_row = []
            for j in range(self.cols):
                result_row.append(self.data[i][j] + other.data[i][j])
            result.append(result_row)
        return Matrix(result)

    def multiply(self, other):
        """Умножение двух матриц.
        
        Аргумент:
        other -- другая матрица (объект класса Matrix)
        
        Возвращает новую матрицу как результат умножения.
        """
        if self.cols != other.rows:
            raise ValueError("Количество столбцов первой матрицы должно совпадать с количеством строк второй матрицы.")
        result = []
        for i in range(self.rows):
            result_row = []
            for j in range(other.cols):
                sum_value = sum(self.data[i][k] * other.data[k][j] for k in range(self.cols))
                result_row.append(sum_value)
            result.append(result_row)
        return Matrix(result)

# Пример использования
matrix1 = Matrix([[1, 2, 3], [4, 5, 6]])
matrix2 = Matrix([[7, 8], [9, 10], [11, 12]])

# Корректное использование метода multiply
matrix_product = matrix1.multiply(matrix2)
print("Результат умножения матриц:")
for row in matrix_product.data:
    print(row)

# Ошибочное использование метода multiply, вызывающее ValueError
# Создадим матрицу, которая не совместима для умножения
matrix3 = Matrix([[1, 2], [3, 4]])

# Эта строка вызовет ошибку ValueError
matrix_product_error = matrix1.multiply(matrix3)