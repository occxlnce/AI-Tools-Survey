﻿# AI Tools Survey Website

web based application designed to conduct a survey on the impact of AI tools on the academic performance of IT students. The survey collects responses through a form and stores the data for further analysis.

## Table of Contents

- [Project Structure](#project-structure)
- [Features](#features)
- [Setup and Installation](#setup-and-installation)
- [Usage](#usage)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)
- [License](#license)

## Project Structure

```
AI_SURVEY
│
├── index.html             # Consent form and information sheet
├── survey.html            # Survey form
├── style.css              # Styling for the web pages
├── script.js              # JavaScript for form handling
├── AI1.jpg                # Hero image
├── favicon.png            # Favicon image
└── README.md              # This file
```

## Features

- **Consent Form**: An initial consent form that participants must agree to before proceeding to the survey.
- **Survey Form**: Collects data on the usage of AI tools and their perceived impact on academic performance.
- **Responsive Design**: The web application is responsive and works well on different devices.
- **Netlify Integration**: Uses Netlify forms for handling form submissions without server-side code.

## Setup and Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/occxlnce/airg.git
    cd airg
    ```

2. **Deploy on Netlify**:
    - Create a new site on Netlify.
    - Link your repository to Netlify.
    - Netlify will automatically detect the `index.html` file and deploy your site.

## Usage

1. **Open the Website**:
    - Navigate to the deployed website.

2. **Complete the Consent Form**:
    - Read the information sheet.
    - Check the consent checkbox and click "Proceed to Survey".

3. **Fill Out the Survey Form**:
    - Answer all the questions on the survey form.
    - Click "Submit" to send your responses.

## Technologies Used

- **HTML**: For structuring the web pages.
- **CSS**: For styling the web pages.
- **JavaScript**: For handling form submission and navigation.
- **Netlify**: For hosting the website and handling form submissions.

## Contributing

Contributions are welcome! If you have any suggestions or improvements, feel free to submit a pull request. Please ensure your changes follow the project's coding guidelines.

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`.
3. Make your changes and commit them: `git commit -m 'Add some feature'`.
4. Push to the branch: `git push origin feature-branch`.
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
