import { useCallback, useEffect, useState } from 'react';
import 'survey-core/defaultV2.min.css';
import { StylesManager, Model } from 'survey-core';
import { Survey } from 'survey-react-ui';

StylesManager.applyTheme("defaultV2");

function App() {
    // load questions
    const [questions, setQuestions] = useState({});
    useEffect(() => {
        fetch("/questions").then((res) =>
            res.json().then((questions) => {
                setQuestions(questions)
            })
        );
    }, []);

    // Create survey model
    const survey = new Model(questions);

    // Send user results to server
    const sendResults = useCallback((sender) => {
         fetch("/complete", {
            method: "POST",
            headers: {
            'Content-Type' : 'application/json'
            },
            body: JSON.stringify(sender.data)
            })
    }, []);
    survey.onComplete.add(sendResults);

    return <Survey model={survey} />;
}

export default App;