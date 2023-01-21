import { useCallback } from 'react';
import 'survey-core/defaultV2.min.css';
import { StylesManager, Model } from 'survey-core';
import { Survey } from 'survey-react-ui';
import data from "./data/data.json";

StylesManager.applyTheme("defaultV2");

function App() {
    const survey = new Model(data);
    // const alertResults = useCallback((sender) => {
    //     const results = JSON.stringify(sender.data);
    //     alert(results);
    // }, []);

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