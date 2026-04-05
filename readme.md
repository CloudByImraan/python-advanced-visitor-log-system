 🧾 Visitor Log System (Python Advanced)

 📌 Description
This is a Python-based visitor logging system that records visitor entries with timestamps.

The system ensures:
- No duplicate visitor entries
- A 5-minute waiting rule between visitors

 Features
- File handling using `with` statement
- Custom exceptions:
  - DuplicateVisitorError
  - TimeRestrictionError
- Automatic file creation if not found
- Timestamp logging
- Error handling without crashing

 🛠️ Technologies Used
- Python
- datetime module
- File handling

 📂 Project Structure
python-advanced-visitor-log-system/
│── visitor_log.py
│── visitors.txt
│── output.txt
│── README.md

 ▶️ How to Run
1. Open project in VS Code
2. Run:
   python visitor_log.py

 💡 Example

Enter visitor's name: Ahmed  
Output:  
Visitor added successfully  

If same visitor tries again:  
Error: Visitor already signed in last  

If within 5 minutes:  
Error: Another visitor cannot enter until after 5 minutes  

 🔮 Future Improvements
- Add GUI interface
- Store data in database
- Add admin dashboard
- Allow multiple visitor tracking

 👨‍💻 Author
Imraan Mu'hd Sani
