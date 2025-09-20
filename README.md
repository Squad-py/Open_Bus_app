# SQUAD.py

- Juan Manuel Ibarra Olvera (utm24090855@utma.edu.mx)

- Hiram Yael Montañez Duron (utm24090330@utma.edu.mx)

- Kevin Gael Valle Martinez (utm24090280@utma.edu.mx)

- Carlos Alejandro Galindo Islas (utm22030587@utma.edu.mx)

## What's the problem? ❔
The public transportation system in Aguascalientes is inefficient due to the lack of real-time information about vehicle location and occupancy, inefficient fleet management, **outdated cash payment processes and inefficiencies in prepaid card recharges that delay boarding**, and the lack of robust data for authorities to make strategic decisions.

## What technology will you use? 💻
The project is based on a combination of modern technologies:
- **Payments: OpenPayments Interledger technology is integrated to enable fast, contactless payments.**
- Artificial Intelligence: Python, OpenCV, and YOLOv5 are used for computer vision processing and real-time passenger counting.
- Backend: Flask and Node.js are used to develop the REST API.
- Database: PostgreSQL is used for data management.
- Frontend (Web/Mobile): Development is done with HTML, CSS, JavaScript, and Leaflet.js for maps. Google Cloud Platform API is also considered as an alternative for geolocation.
- Accessibility: The UserWay tool is integrated to ensure the platform is accessible to people with disabilities.

## What's the solution? 📝
The solution, called OpenBus, is a comprehensive platform that modernizes public transportation. It combines a **digital payment system**, onboard sensors that measure vehicle occupancy in real time, a data management platform that uses AI to optimize routes, and a mobile app so users can plan their trips efficiently, check bus occupancy, and pay electronically.

## What are the benefits? ✔️
The benefits extend to all stakeholders:
- For users: Greater safety, comfort, and the ability to plan their trips. They can check real-time occupancy and **top up their prepaid cards online.**
- For operators and the city: The system enables fleet distribution optimization, leading to more efficient resource use and more profitable operations. It also provides authorities with evidence-based decision-making tools.
- At a social level: It improves citizens' quality of life, makes transportation more accessible for people with disabilities, and promotes safer, more efficient mobility.

## What's your simple architecture/stack? 👨‍💻
The technology stack is as follows:
- Frontend: HTML, CSS, JavaScript, Leaflet.js, and optionally Google Cloud Platform API.
- Backend: Python with Flask, Node.js, and OpenCV/YOLOv5.
- Database: PostgreSQL.
- Integrations: OpenPayments Interledger and UserWay.
- The architecture is modular, with separate components communicating through an API.

## What functions are essential? ❕
The key functions are:
- Online payment system: For prepaid card recharges.
- Real-time passenger counting: To determine bus occupancy.
- Geolocation and maps: To display bus locations.
- Data management dashboard: For analysis and decision-making by authorities.
- Accessibility: Integration of UserWay to ensure inclusive use of the platform.

## Who will be responsible for building what part?
Team responsibilities are divided as follows:
- Hiram Yael Montañez Duron: Project Leader.
- Kevin Gael Valle Martinez: Developer.
- Carlos Alejandro Galindo Islas: Database Manager (DB Manager).
- Juan Manuel Ibarra Olvera: Developer.

## How to run locally?
Execute
```
      git clone https://github.com/Squad-py/Open_Bus_app.git
      cd Open_Bus_app/
      npm i
      node OP_forOpenBus.js
```

Open other terminal and then
```
      python -m venv venv
      .\venv\Scripts\activate
      pip install -r requirements.txt
      python app.py
```

Finally open in localhost (port 5000)


