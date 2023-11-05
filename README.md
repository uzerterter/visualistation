# InfoVis2324

This README.md provides an overview of our university project for the Information Visualization lecture. The goal of this project is to design and develop a website that effectively visualizes a given dataset to help gain new insights and make data-driven decisions. The project will be a culmination of our understanding of data visualization techniques, web development, and the principles of effective communication.

## Authors & Contributors

- Product Owner
    - Lara Moric
- SCRUM Master
    - Ludwig Degenhardt
- Developers
  - Chief of Design
    - Linus Stetter
  - Andrian Melnikov
  - Rebecca Fendt
    

## Project Description

### Dataset

- [Traffic Genesis](https://www-genesis.destatis.de/genesis//online?operation=table&code=46181-0015&bypass=true&levelindex=0&levelid=1697718366080#abreadcrumb)
- supplementary datasets

### Goals

1. Visualizing the relationship between traffic data and economic factors in the individual german federal states
2. Making visualizations interactive and exciting applying various concepts from the lecture
3. Ensuring clarity and accessibility through intelligent, appealing design

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
    - Trello for task management

## Installation

1. Clone this repository

    ```bash
    git clone https://gitlab.lrz.de/iv2324-projects/team08.git
    ```

2. Install necessary dependencies

    ```bash
    npm install
    ```

3. Start a development server

    ```bash
    npm run dev

    # or start the server and open the app in a new browser tab
    npm run dev -- --open
    ```

4. Build the App

    To build your library:

    ```bash
    npm run package
    ```

    To create a production version of your showcase app:

    ```bash
    npm run build
    ```

    You can preview the production build with `npm run preview`.

    > To deploy your app, you may need to install an [adapter](https://kit.svelte.dev/docs/adapters) for your target environment.

## License

