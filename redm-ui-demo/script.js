const sendLetter =
    document.getElementById("sendLetter");

const modal =
    document.getElementById("letterModal");

const closeModal =
    document.getElementById("closeModal");

const search =
    document.getElementById("search");


sendLetter.addEventListener(
    "click",
    () => {

        modal.classList.add(
            "visible"
        );

    }
);


closeModal.addEventListener(
    "click",
    () => {

        modal.classList.remove(
            "visible"
        );

    }
);


search.addEventListener(
    "input",
    (event) => {

        const value =
            event.target.value
                .toLowerCase();

        document
            .querySelectorAll(
                ".mail-item"
            )
            .forEach(mail => {

                const visible =
                    mail.innerText
                        .toLowerCase()
                        .includes(value);

                mail.style.display =
                    visible
                        ? "flex"
                        : "none";
            });

    }
);
