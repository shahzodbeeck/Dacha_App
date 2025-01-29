# Qoidalar

Shu loyihada ishlashda quyidagi qoidalarni doimo yodda tuting va ularga amal qiling.

---

## 1). Yangi kutubxona qo‘shilganda

- Har safar yangi kutubxona o‘rnatilgandan keyin loyihangizning `requirements.txt` faylini yangilab turing:

```bash
pip freeze > requirements.txt
```

Python'da funksiyalar uchun izoh (docstring) yozish qoidalari kodning tushunarli va qulay bo‘lishini taʼminlaydi. Quyida
to‘liq docstring yozish tartibi keltirilgan.

---
2). Docstring yozish qoidalari

## 1. Docstring nima?

- Docstring (dokumentatsiya qatori) — funksiyaning nima ish qilishini, qanday parametrlarni qabul qilishini va qanday
  qiymatni qaytarishini tushuntirish uchun yozilgan matn.
- Docstring har bir funksiyaning birinchi qatorida uchta qo‘shtirnoq (`"""`) ichida yoziladi.

---

## 2. Docstring yozish qoidalari

### Umumiy format

Quyidagi formatga amal qiling:

### 1.Funksiyalar uchun docstring yozish

```python
def function_name(param1, param2):
    """
    Funksiya tavsifi: Funksiyaning nima ish qilishi haqida qisqacha tushuntirish.

    Parameters:
        param1 (tip): Parametrning tavsifi.
        param2 (tip): Parametrning tavsifi.

    Returns:
        tip: Funksiyaning qaytaradigan qiymati haqida tushuntirish.
    """
    # Funksiya kodi
    pass
```

### 2. Class uchun docstring yozish

```python
class ClassName:
    """
    Class tavsifi: Classning nima ish qilishi haqida qisqacha tushuntirish.

    Attributes:
        attribute1 (tip): Atributning tavsifi.
        attribute2 (tip): Atributning tavsifi.

    Methods:
        method_name(param1, param2):

            Method tavsifi: Methodning nima ish qilishi haqida qisqacha tushuntirish.

            Parameters:
                param1 (tip): Parametrning tavsifi.
                param2 (tip): Parametrning tavsifi.

            Returns:
                tip: Methodning qaytaradigan qiymati haqida tushuntirish.
            """
```

### 3. Serializers uchun docstring yozish

```python
class ClassName:
    """
    class Meta:
        model = ModelName
        fields = ['field1', 'field2']
        depth = 2
        serializers uchun docstring yozish
        
  """

```