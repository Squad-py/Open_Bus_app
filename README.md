![Banner del proyecto OpenBus](OpenBus.jpg)






SQUAD.py


Juan Manuel Ibarra Olvera 
utm24090855@utma.edu.mx

Hiram Yael Montañez Duron 
utm24090330@utma.edu.mx

Kevin Gael Valle Martinez 
utm24090280@utma.edu.mx

Carlos Alejando Galindo Islas
utm22030587@utma.edu.mx











¿Cuál es el problema?
El sistema de transporte público de Aguascalientes es ineficiente debido a la falta de información en tiempo real sobre la ubicación y ocupación de las unidades, la ineficiente gestión de flotas, los obsoletos procesos de pago en efectivo que retrasan el abordaje y la falta de datos robustos para que las autoridades tomen decisiones estratégicas.

¿Qué tecnología usarán?
El proyecto se basa en una combinación de tecnologías modernas:
Inteligencia Artificial: Se utilizan Python, OpenCV y YOLOv5 para el procesamiento de visión por computadora y el conteo de pasajeros en tiempo real.
Pagos: Se integra la tecnología Interledger de OpenPayments para permitir pagos rápidos y sin contacto.
Backend: Se emplean Flask y Node.js para el desarrollo de la API REST.
Base de Datos: Se utiliza PostgreSQL para la gestión de la información.
Frontend (Web/Móvil): El desarrollo se realiza con HTML, CSS, JavaScript y Leaflet.js para mapas. También se considera la API de Google Cloud Platform como alternativa para la geolocalización.
Accesibilidad: Se integra la herramienta UserWay para garantizar que la plataforma sea accesible para personas con discapacidades.







¿Cuál es la solución?
La solución, llamada OpenBus, es una plataforma integral que moderniza el transporte público. Combina un sistema de pagos digital, sensores a bordo que miden la ocupación de las unidades en tiempo real, una plataforma de gestión de datos que usa IA para optimizar rutas, y una aplicación móvil para que los usuarios puedan planificar sus viajes de manera eficiente, ver la ocupación de los autobuses y pagar de forma electrónica.

¿Cuáles son los beneficios?
Los beneficios son para todos los involucrados:
Para los usuarios: Mayor seguridad, comodidad y la posibilidad de planificar sus viajes. Pueden ver la ocupación de las unidades en tiempo real y recargar sus tarjetas de prepago en línea.
Para los operadores y la ciudad: El sistema permite optimizar la distribución de la flota, lo que se traduce en un uso más eficiente de los recursos y una operación más rentable. Además, facilita a las autoridades la toma de decisiones basada en evidencia.
A nivel social: Mejora la calidad de vida de los ciudadanos, hace el transporte más accesible para personas con discapacidades y promueve una movilidad más segura y eficiente.

¿Cuál es su arquitectura/stack simple?
El stack tecnológico es el siguiente:
Frontend: HTML, CSS, JavaScript, Leaflet.js y la API de Google Cloud Platform (opcional).
Backend: Python con Flask, Node.js y OpenCV/YOLOv5.
Base de Datos: PostgreSQL.
Integraciones: Interledger de OpenPayments y UserWay. La arquitectura es modular, con distintos componentes que se comunican a través de una API.

¿Qué funciones son indispensables?
Las funciones clave son:
Conteo de pasajeros en tiempo real: Para determinar la ocupación de las unidades.
Geolocalización y mapas: Para visualizar la ubicación de los autobuses.
Sistema de pagos en línea: Para las recargas a la tarjeta de prepago.
Panel de gestión de datos: Para el análisis y la toma de decisiones por parte de las autoridades.
Accesibilidad: La integración de UserWay para garantizar un uso inclusivo de la plataforma.

¿Quién será responsable de construir qué parte?
La responsabilidad del equipo se distribuye de la siguiente manera:
Hiram Yael Montañez Duron: Líder del proyecto.
Kevin Gael Valle Martinez: Desarrollador.
Carlos Alejandro Galindo Islas: Administrador de la base de datos (DB Manager).
Juan Manuel Ibarra Olvera: Desarrollador.









•What's the problem?
The public transportation system in Aguascalientes is inefficient due to a lack of real-time information on vehicle location and occupancy, inefficient fleet management, obsolete cash payment processes that delay boarding, and a lack of robust data for authorities to make strategic decisions.

•What technology will you use?
The project is based on a combination of modern technologies:
Artificial Intelligence: Python, OpenCV, and YOLOv5 are used for computer vision processing and real-time passenger counting.
Payments: OpenPayments Interledger technology is integrated to allow for fast, contactless payments.
Backend: Flask and Node.js are used to develop the REST API.
Database: PostgreSQL is used for information management.
Frontend (Web/Mobile): Development is done with HTML, CSS, JavaScript, and Leaflet.js for maps. The Google Cloud Platform API is also considered as an alternative for geolocation.
Accessibility: The UserWay tool is integrated to ensure the platform is accessible to people with disabilities.

•What's the solution?
The solution, called OpenBus, is a comprehensive platform that modernizes public transportation. It combines a digital payment system, onboard sensors that measure vehicle occupancy in real time, a data management platform that uses AI to optimize routes, and a mobile app so users can plan their trips efficiently, see bus occupancy, and pay electronically.

•What are the benefits?
The benefits are for everyone involved:
For users: Greater safety, comfort, and the ability to plan their trips. They can see unit occupancy in real time and top up their prepaid cards online.
For operators and the city: The system allows for optimizing fleet distribution, which leads to a more efficient use of resources and a more profitable operation. It also enables authorities to make evidence-based decisions.
On a social level: It improves citizens' quality of life, makes transportation more accessible for people with disabilities, and promotes safer, more efficient mobility.

•What's your simple architecture/stack?
The technological stack is as follows:
Frontend: HTML, CSS, JavaScript, Leaflet.js, and the Google Cloud Platform API (optional).
Backend: Python with Flask, Node.js, and OpenCV/YOLOv5.
Database: PostgreSQL.
Integrations: OpenPayments Interledger and UserWay. The architecture is modular, with different components communicating through an API.

•What functions are essential?
The key functions are:
Real-time passenger counting: To determine unit occupancy.
Geolocation and maps: To visualize bus locations.
Online payment system: For prepaid card top-ups.
Data management dashboard: For analysis and decision-making by authorities.
Accessibility: The integration of UserWay to ensure inclusive use of the platform.

•Who will be responsible for building what part?
The team's responsibilities are distributed as follows:
Hiram Yael Montañez Duron: Project Leader.
Kevin Gael Valle Martinez: Developer.
Carlos Alejandro Galindo Islas: DB Manager.
Juan Manuel Ibarra Olvera: Developer.


