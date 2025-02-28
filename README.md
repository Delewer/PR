# PR – Laborator 1  

## 📌 Descriere  
Acest depozit conține prima lucrare de laborator la disciplina **PR**. Proiectul reprezintă un **chat în consolă** scris în Python, format dintr-un server și un client.  

## 🚀 Funcționalitate  
- Serverul acceptă conexiuni de la mai mulți clienți.  
- Clienții pot trimite mesaje care sunt distribuite tuturor utilizatorilor conectați.  
- Comunicarea se realizează prin socket-uri (TCP).  

## 🛠 Instalare și rulare  

### 🔹 Cerințe  
- Python 3.x  
- Modulul `socket` (inclus în biblioteca standard)  

### 🔹 Instalare  
1. Clonați depozitul:  
   ```bash
   git clone https://github.com/Delewer/PR.git
   cd PR
   ```

### 🔹 Pornirea serverului  
```bash
python server.py
```

### 🔹 Pornirea clientului  
```bash
python client.py
```

## 📖 Utilizare  
1. Porniți serverul (`server.py`).  
2. Deschideți mai mulți clienți (`client.py`).  
3. Introduceți un mesaj în consola clientului – acesta va fi transmis tuturor utilizatorilor conectați.  

## 📜 Licență  
Acest proiect a fost realizat în scopuri educaționale.
