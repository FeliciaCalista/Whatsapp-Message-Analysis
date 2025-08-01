# WhatsApp Message Analysis

This project is a **Python-based data analysis tool** designed to visualize insights from a WhatsApp group chat export. It uses `matplotlib` to generate 4 visualizations based on the uploaded `.txt` chat file.

---

## Features

- **Find the 3 busiest chat days** and their hourly distribution
- **Pie chart of top contributors** (who sends the most messages)
- **Bar chart of top 5 most-used words** (excluding media)
- **Bar chart of total messages per day** (full week view)

---

## Technologies Used

- Python 3.x
- [matplotlib](https://matplotlib.org/)

> All data processing is done with basic Python (no Pandas required).

---

## Input Format

Your WhatsApp exported chat file should be named: "Whatsapp Message"
Each line in the file must follow this format: DD/MM/YYYY, HH:MM - Name: Message

## Output Charts
- Line chart showing chat activity over the 3 busiest days by hour
- Pie chart showing who sent the most messages
- Bar chart of top 5 words 
- Bar chart of messages sent per day (1-week snapshot)

## License

This project is licensed under the **MIT License** – you are free to use, modify, and distribute this project with attribution.

## Contributors
- [@pompom-cl](https://github.com/pompom-cl)
- [@FeliciaCalista](https://github.com/FeliciaCalista)
- [@gracehutapea1208](https://github.com/gracehutapea1208)
