APP_STYLE = """
/* ------------------------------------------------ */
/* Main Window */
/* ------------------------------------------------ */
QProgressBar {
    border: none;
    border-radius: 8px;
    background-color: #2B2B2B;
    height: 16px;
    text-align: center;
    color: white;
    font-weight: bold;
}

QProgressBar::chunk {
    background-color: #4CAF50;
    border-radius: 8px;
}
QMainWindow {
    background-color: #0F1117;
}

QWidget {
    background-color: #0F1117;
    color: #F3F4F6;
    font-family: "Segoe UI";
    font-size: 11pt;
}

/* ------------------------------------------------ */
/* Cards */
/* ------------------------------------------------ */

#Card {
    background-color: #1A1D24;
    border: 1px solid #2B303B;
    border-radius: 16px;
}

#Card:hover {
    border: 1px solid #4F8CFF;
}

/* ------------------------------------------------ */
/* Card Labels */
/* ------------------------------------------------ */

#CardTitle {
    color: #9CA3AF;
    font-size: 12pt;
    font-weight: bold;
}

#CardValue {
    color: #FFFFFF;
    font-size: 28pt;
    font-weight: bold;
}

#CardSubtitle {
    color: #6B7280;
    font-size: 10pt;
}

/* ------------------------------------------------ */
/* Header */
/* ------------------------------------------------ */

QLabel {
    background: transparent;
}
"""