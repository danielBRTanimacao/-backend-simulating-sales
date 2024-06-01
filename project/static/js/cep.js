(function () {
    const cep = document.querySelector("input[name=CEP]");

    cep.addEventListener("blur", (e) => {
        const value = cep.value.replace(/[^0-9]+/, "");
        const url = `https://viacep.com.br/ws/${value}/json/`;

        fetch(url)
            .then((response) => response.json())
            .then((json) => {});
    });
})();
