🔑 Password Generator

📝 Description

This is a 🐍 Python-based 🔑 password generator that allows users to 🔀 generate secure 🔐 passwords and store them in an 📊 Excel file (passwords.xlsx). The generated passwords follow a 📏 structured pattern with a ✨ unique mark (s120802) inserted at different positions based on the ⚖️ importance level chosen by the user.

🚀 Features

🔐 Generate strong passwords with customizable length.

⚖️ User-defined importance levels:

    🔴 High Importance → Includes 's1'

    🟠 Medium Importance → Includes '208'

    🟢 Low Importance → Includes '02'

📂 Stores passwords, usernames, and website links in an 📊 Excel file.

🚫 Prevents overwriting issues and 📏 auto-adjusts column widths in the Excel file.

⚠️ Error handling for missing inputs and incorrect values.

🔧 Installation

📌 Prerequisites

Ensure you have 🐍 Python 3 installed. If not, download it from 🌍 python.org.

📥 Install Required Libraries

Run the following command to install the necessary dependencies:

pip install pandas openpyxl

🏃 Usage

▶️ Run the Script

🖥️ Open your terminal or command prompt.

📂 Navigate to the project directory:

cd path/to/password-generator

▶️ Run the script:

python app.py

🔢 User Inputs

The program will prompt the user for:

👤 Username → The login name for the account.

🌐 Website URL → The website or service where the password will be used.

⚖️ Password Importance Level:

Enter 1️⃣ for Low

Enter 2️⃣ for Medium

Enter 3️⃣ for High

🔢 Password Length → The number of characters for the password.

🖥️ Example Interaction

Enter your 👤 username: user123
Enter the 🌐 website URL: https://example.com
Enter password ⚖️ importance level (1️⃣ Low, 2️⃣ Medium, 3️⃣ High): 3️⃣
Enter the number of 🔢 digits for the password: 16

✅ Password saved successfully!

🔐 Your password for https://example.com is: AbC!s1Xy@123

📂 File Structure

password-generator/
│-- app.py  # 🖥️ Main script
│-- passwords.xlsx  # 📊 Excel file where passwords are stored
│-- README.md  # 📖 Documentation

🔮 Future Improvements

🖥️ Graphical User Interface (GUI) 🎨 using Tkinter.

🔏 Encryption for stored passwords for added security.

🗄️ Password retrieval system with authentication.

🤝 Contributing

If you'd like to contribute, feel free to 🍴 fork this repository and submit a 📩 pull request!
