import { useCallback, useEffect, useState } from 'react';
import 'survey-core/defaultV2.min.css';
import { StylesManager, Model } from 'survey-core';
import { Survey } from 'survey-react-ui';

StylesManager.applyTheme("defaultV2");

function App() {
    // usestate for setting a javascript
    // object for storing and using data
    const [questions, setQuestions] = useState({});

    // Using useEffect for single rendering
    useEffect(() => {
        // Using fetch to fetch the api from 
        // flask server it will be redirected to proxy
        fetch("/questions").then((res) =>
            res.json().then((questions) => {
                // Setting a data from api
                setQuestions(questions)
            })
        );
    }, []);

    // Create survey model
    const survey = new Model(questions);

    const alertResults = useCallback((sender) => {
        const response = fetch("/add_todo", {
            method: "POST",
            headers: {
            'Content-Type' : 'application/json'
            },
            body: JSON.stringify(sender.data)
            })
            if (response.ok){
            console.log("it worked")}
    }, []);

    survey.onComplete.add(alertResults);

    return <Survey model={survey} />;
}

export default App;