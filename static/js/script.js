document.addEventListener("DOMContentLoaded", function() {
    const form = document.getElementById("myForm");
    const modalContainer = document.getElementById("modalContainer");
    const modalMessage = document.getElementById("modalMessage");
    const closeButton = document.querySelector(".close-button");

    // form.addEventListener("submit", async function(event) {
    //     event.preventDefault();
    //     const inputField = document.getElementById("inputField");
    //     const inputValue = inputField.value;

    //     try {
    //         // const response = await fetch("/submit", {
    //         //     method: "POST",
    //         //     headers: {
    //         //         "Content-Type": "application/json"
    //         //     },
    //         //     body: JSON.stringify({ input_value: inputValue })
    //         // });

    //         const response = await fetch("/submit", {
    //             method: "POST",
    //             headers: {
    //                 "Content-Type": "application/json"
    //             },
    //             body: JSON.stringify({ input_value: inputValue })
    //         });
            
    //         const data = await response.json();
    //         modalMessage.textContent = data.message;
    //         modalContainer.style.display = "block";
    //     } catch (error) {
    //         console.error("Ошибка:", error);
    //     }
    // });



    form.addEventListener("submit", async function(event) {
        event.preventDefault();
        const inputField = document.getElementById("inputField");
        const inputValue = inputField.value;
    
        try {
            const response = await fetch("/submit", {
                method: "POST",
                headers: {
                    "Content-Type": "application/json"
                },
                body: JSON.stringify({ input_value: inputValue })
            });
            const data = await response.json();
            modalMessage.textContent = data.message;
            modalContainer.style.display = "block";
        } catch (error) {
            console.error("Ошибка:", error);
        }
    });
    

    closeButton.addEventListener("click", function() {
        modalContainer.style.display = "none";
    });

    window.addEventListener("click", function(event) {
        if (event.target == modalContainer) {
            modalContainer.style.display = "none";
        }
    });
});


// form.addEventListener("submit", async function(event) {
//     event.preventDefault();
//     const inputField = document.getElementById("inputField");
//     const inputValue = inputField.value;

//     try {
//         const response = await fetch("/submit", {
//             method: "POST",
//             headers: {
//                 "Content-Type": "application/json"
//             },
//             body: JSON.stringify({ input_value: inputValue })
//         });
//         const data = await response.json();
//         modalMessage.textContent = data.message;
//         modalContainer.style.display = "block";
//     } catch (error) {
//         console.error("Ошибка:", error);
//     }
// });
