import student

# ---------------- GRADE S ----------------
def test_grade_S_lower():
    assert student.calculate_grade(90) == "S"

def test_grade_S_middle():
    assert student.calculate_grade(95) == "S"

def test_grade_S_upper():
    assert student.calculate_grade(100) == "S"


# ---------------- GRADE A ----------------
def test_grade_A_lower():
    assert student.calculate_grade(80) == "A"

def test_grade_A_middle():
    assert student.calculate_grade(85) == "A"

def test_grade_A_upper():
    assert student.calculate_grade(89.99) == "A"


# ---------------- GRADE B ----------------
def test_grade_B_lower():
    assert student.calculate_grade(65) == "B"

def test_grade_B_middle():
    assert student.calculate_grade(72) == "B"

def test_grade_B_upper():
    assert student.calculate_grade(79.99) == "B"


# ---------------- GRADE C ----------------
def test_grade_C_lower():
    assert student.calculate_grade(50) == "C"

def test_grade_C_middle():
    assert student.calculate_grade(58) == "C"

def test_grade_C_upper():
    assert student.calculate_grade(64.99) == "C"


# ---------------- GRADE D ----------------
def test_grade_D_lower():
    assert student.calculate_grade(40) == "D"

def test_grade_D_middle():
    assert student.calculate_grade(45) == "D"

def test_grade_D_upper():
    assert student.calculate_grade(49.99) == "D"


# ---------------- GRADE F ----------------
def test_grade_F():
    assert student.calculate_grade(30) == "F"