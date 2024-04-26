//  Immediately-Invoked Function Expression (IIFE)
; (atlas => {

    const name = atlas.document.getElementById("nome");

    const phone = atlas.document.getElementById("telefone");

    const card = atlas.document.getElementById("cartaoSUS");

    const street = atlas.document.getElementById("rua");

    const number = atlas.document.getElementById("numero");

    const complement = atlas.document.getElementById("complemento")

    const reference = atlas.document.getElementById("pontoReferencia")

    name.focus();

    name.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 50);

        event.target.value = atlas.replace(event.target.value, atlas.alpha);

    });

    phone.addEventListener("input", event => {

        if (event.inputType === "insertText") {
            event.target.value = atlas.mask(event.target.value)
        }
    });

    card.addEventListener('input', event => event.target.value = atlas.maximum(event.target.value, 15));

    street.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 50);

        event.target.value = atlas.replace(event.target.value, atlas.alphaNumeric);

    });

    number.addEventListener("input", event => event.target.value = atlas.maximum(event.target.value, 5));

    complement.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 40);

        event.target.value = atlas.replace(event.target.value, atlas.alphaNumeric);

    });

    reference.addEventListener("input", event => {

        event.target.value = atlas.maximum(event.target.value, 40);

        event.target.value = atlas.replace(event.target.value, atlas.alphaNumeric);

    });

    atlas.window.addEventListener('beforeunload', event => {
        console.log("Atlas sendo encerrado");
    });

})({
    document,
    window,
    "alpha": alpha,
    "alphaNumeric": alphaNumeric,
    "mask": maskPhone,
    "replace": replaceCharacter,
    "maximum": maximumCharacters
})