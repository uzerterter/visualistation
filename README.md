# InfoVis2324

This README.md provides an overview of our university project for the Information Visualization lecture. The goal of
this project is to design and develop a website that effectively visualizes a traffic data of germany to help gain new
insights and make data-driven decisions. The project is a culmination of our understanding of data visualization
techniques, web development, and the principles of effective communication.

## Authors & Contributors

| Member            | Role          | Current Position                           |
|-------------------|---------------|--------------------------------------------|
| Lara Moric        | Product Owner | LMU München, Medieninformatik BA           |
| Ludwig Degenhardt | SCRUM Master  | LMU München, Human-Computer-Interaction MA |
| Linus Stetter     | Design        | LMU München, Informatik MA                 |
| Andrian Melnikov  | Developer     | LMU München, Informatik MA                 |
| Rebecca Fendt     | Developer     | LMU München, Human-Computer-Interaction MA |

### Dataset

- [Traffic Genesis](https://www-genesis.destatis.de/genesis//online?operation=table&code=46181-0015&bypass=true&levelindex=0&levelid=1697718366080#abreadcrumb)  

**For own inspection of our sources please refer to our sources page on our live website**
- Population density (per squarekilometer )
- Population numbers
- Unemployment rate
- Average annual gross employee income

### Research Questions

##### RQ1: Is there a connection between the use of local public transport and economic factors at federal and state level?
There seems to be a negative correlation between the unemployment rate in a federal state and the residents usage of puplic transportation means: The higher the unemployment rate, the lower the usage of bus, tram or train.

##### RQ2: Is there a connection between the use of public transportation and population data in the federal and state governments?
In general there is a positive correlation between the population density and the public transportation usage: The higher the population density the more residents use busses, trams or trains. 

### Goals

1. Visualizing the relationship between traffic data and economic factors in the individual german federal states
2. Make visualisations interactive and engaging for a good user experience
3. Ensure usability and accessibility through intelligent, appealing design

### Technologies

We will be using the following technologies to build our website:

- **Frontend**
    - Svelte with Javascript for functionalities
    - D3.js for data visualization
- **Data**
    - Python Pandas for data manipulation
- **Version Control**
    - GitLab for collaborative development
- **SCRUM**
    - LRZ Gitlab Issues for issue organization and tracking
    - Team Gantt for progress tracking

## Link to Site

**[Here](https://iv2324-projects.pages.gitlab.lrz.de/team08/)** you can find our hosted visualization website.

## Feature List
- **Timeline**
- **Map**
- **For the Economic Datasets**
    - Barchart (Left)
    - Doughnutchart (Left)
    - Horizontal-Barchart (Left)

- **For The Genesis Dataset**
    - Barchart (Right)
    - Doughnutchart (Right)
    - Horizontal-Barchart (Right)

## Installation

1. Clone this repository

    ```bash
    git clone https://gitlab.lrz.de/iv2324-projects/team08.git
    ```

2. Create a Python virtual environment (optional but recommended)

    ```bash
    python -m venv venv
    ```

   Activate the virtual environment:

    - On Windows:

        ```bash
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```bash
        source venv/bin/activate
        ```

3. Install necessary Python dependencies

    ```bash
    pip install -r requirements.txt
    ```

4. Install necessary JavaScript dependencies

    ```bash
    npm install
    ```

5. Start a development server

    ```bash
    npm run dev

    # or start the server and open the app in a new browser tab
    npm run dev -- --open
    ```

6. Build the App

   To build your library:

    ```bash
    npm run package
    ```

   To create a production version of your showcase app:

    ```bash
    npm run build
    ```

   You can preview the production build with `npm run preview`.

   > To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target
   environment.

## Roadmap

### Implemented & Tested

The following features have been successfully implemented
- **Map** of Germany and its federal states with color coding to show the population density in each state
- **Doughnut charts** to show the distribution among the individual federal states with regard to various factors
- **Bar charts** to show the development over time 
- **Horizontal bar charts** showing a comparison between different federal states with regard to various factors
- **Timeline** connected to all of the above for control 


