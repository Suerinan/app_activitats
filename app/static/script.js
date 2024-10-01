const Constants = {
    POST: "POST",
    PUT: "PUT",
    GET: "GET",
    DELETE: "DELETE",
    REGISTRAR_USUARI: "Registrar usuari",
    ACTUALITZAR_USUARI: "Actualitzar usuari",
    OBTENIR_INFO_USUARI: "Obtenir info. usuari",
    ELIMINAR_USUARI: "Eliminar usuari",
    CREAR_ACTIVITAT: "Crear activitat",
    CONSULTAR_ACTIVITATS: "Consultar activitats",
    APUNTAR_ACTIVITATS: "Apuntar-se a activitat",
    URL_USUARI: "/user",
    URL_ACTIVITAT: "/activitat",
    URL_APP: "/appActivitats",
    URL_APUNTAR_USUARI: "/apuntar_usuari"
};

function netejarFormularis() {
    document.getElementById('registrar-usuari-form').innerHTML = '';
    document.getElementById('actualitza-usuari-form').innerHTML = '';
    document.getElementById('elimina-usuari-form').innerHTML = '';
    document.getElementById('selecciona-usuari-info-form').innerHTML = '';
    document.getElementById('crear-activitat-form').innerHTML = '';
    document.getElementById('consultar-activitats-form').innerHTML = '';
    document.getElementById('apuntar-activitat-form').innerHTML = '';
}

function mostrarBotoEnviar(messageType, btnText) {
    const btEnvia = document.getElementById("submit");
    btEnvia.hidden = false;
    btEnvia.setAttribute("type_message", messageType);
    btEnvia.setAttribute("btn_action", btnText)
    btEnvia.textContent = btnText
}

function crearDni(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'dni');
    label.textContent = 'Dni: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'dni');
    input.setAttribute('name', 'dni');
    input.setAttribute('placeholder', 'Entri el dni');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearNom(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'nom');
    label.textContent = 'Nom: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'nom');
    input.setAttribute('name', 'nom');
    input.setAttribute('placeholder', 'Entri el nom');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearCognoms(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'cognoms');
    label.textContent = 'Cognoms: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'cognoms');
    input.setAttribute('name', 'cognoms');
    input.setAttribute('placeholder', 'Entri els cognoms');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearEdat(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'edat');
    label.textContent = 'Edat: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'edat');
    input.setAttribute('name', 'edat');
    input.setAttribute('placeholder', 'Entri l\'edat');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearContrasenya(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'contrasenya');
    label.textContent = 'Contrasenya: ';

    const input1 = document.createElement('input');
    input1.setAttribute('type', 'password');
    input1.setAttribute('id', 'contrasenya1');
    input1.setAttribute('name', 'contrasenya');
    input1.setAttribute('placeholder', 'Entri la contrasenya');
    input1.setAttribute('required', 'required');

    const input2 = document.createElement('input');
    input2.setAttribute('type', 'password');
    input2.setAttribute('id', 'contrasenya2');
    input2.setAttribute('name', 'contrasenya');
    input2.setAttribute('placeholder', 'Reentri la contrasenya');
    input2.setAttribute('required', 'required');

    return [label, input1, input2];
}

function registrarUsuari() {
    netejarFormularis();
    const formContainer = document.getElementById('registrar-usuari-form');
    
    const dni = crearDni(document);
    const nom = crearNom(document);
    const cognoms = crearCognoms(document);
    const edat = crearEdat(document);
    const contrasenya = crearContrasenya(document);

    formContainer.appendChild(dni[0]);
    formContainer.appendChild(dni[1]);
    formContainer.appendChild(nom[0]);
    formContainer.appendChild(nom[1]);
    formContainer.appendChild(cognoms[0]);
    formContainer.appendChild(cognoms[1]);
    formContainer.appendChild(edat[0]);
    formContainer.appendChild(edat[1]);
    formContainer.appendChild(contrasenya[0]);
    formContainer.appendChild(contrasenya[1]);
    formContainer.appendChild(contrasenya[2]);

    mostrarBotoEnviar(Constants.POST, Constants.REGISTRAR_USUARI);
}

function actualitzarUsuari() {
    netejarFormularis();
    const formContainer = document.getElementById('actualitza-usuari-form');

    const dni = crearDni(document);
    const nom = crearNom(document);
    const cognoms = crearCognoms(document);
    const edat = crearEdat(document);
    const contrasenya = crearContrasenya(document);

    formContainer.appendChild(dni[0]);
    formContainer.appendChild(dni[1]);
    formContainer.appendChild(nom[0]);
    formContainer.appendChild(nom[1]);
    formContainer.appendChild(cognoms[0]);
    formContainer.appendChild(cognoms[1]);
    formContainer.appendChild(edat[0]);
    formContainer.appendChild(edat[1]);
    formContainer.appendChild(contrasenya[0]);
    formContainer.appendChild(contrasenya[1]);
    formContainer.appendChild(contrasenya[2]);

    mostrarBotoEnviar(Constants.PUT, Constants.ACTUALITZAR_USUARI);
}

function seleccionarInfoUsuaris() {
    netejarFormularis();
    const formContainer = document.getElementById('selecciona-usuari-info-form');

    const dni = crearDni(document);

    formContainer.appendChild(dni[0]);
    formContainer.appendChild(dni[1]);

    mostrarBotoEnviar(Constants.GET, Constants.OBTENIR_INFO_USUARI);
}

function eliminarUsuari() {
    netejarFormularis();
    const formContainer = document.getElementById('elimina-usuari-form');

    const dni = crearDni(document);

    formContainer.appendChild(dni[0]);
    formContainer.appendChild(dni[1]);

    mostrarBotoEnviar(Constants.DELETE, Constants.ELIMINAR_USUARI);
}

function crearNomActivitat(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'nomActivitat');
    label.textContent = 'Nom de l\'activitat: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'nomActivitat');
    input.setAttribute('name', 'nomActivitat');
    input.setAttribute('placeholder', 'Entri el nom de l\'activitat');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearDescripcioActivitat(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'descripcioActivitat');
    label.textContent = 'Descripció: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'text');
    input.setAttribute('id', 'descripcioActivitat');
    input.setAttribute('name', 'descripcioActivitat');
    input.setAttribute('placeholder', 'Entri la descripció de l\'activitat');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearDataActivitat(document) {
    const label = document.createElement('label');
    label.setAttribute('for', 'dataActivitat');
    label.textContent = 'Data: ';

    const input = document.createElement('input');
    input.setAttribute('type', 'date');
    input.setAttribute('id', 'dataActivitat');
    input.setAttribute('name', 'dataActivitat');
    input.setAttribute('required', 'required');

    return [label, input];
}

function crearActivitat() {
    netejarFormularis();
    const formContainer = document.getElementById('crear-activitat-form');

    const nomActivitat = crearNomActivitat(document);
    const descripcioActivitat = crearDescripcioActivitat(document);
    const dataActivitat = crearDataActivitat(document);

    formContainer.appendChild(nomActivitat[0]);
    formContainer.appendChild(nomActivitat[1]);
    formContainer.appendChild(descripcioActivitat[0]);
    formContainer.appendChild(descripcioActivitat[1]);
    formContainer.appendChild(dataActivitat[0]);
    formContainer.appendChild(dataActivitat[1]);

    mostrarBotoEnviar(Constants.POST, Constants.CREAR_ACTIVITAT);
}

function consultarActivitats() {
    netejarFormularis();
    mostrarBotoEnviar(Constants.GET, Constants.CONSULTAR_ACTIVITATS);
}

function apuntarUsuariActivitat() {
    netejarFormularis();
    const formContainer = document.getElementById('apuntar-activitat-form');

    const dni = crearDni(document);
    const nomActivitat = crearNomActivitat(document);

    formContainer.appendChild(dni[0]);
    formContainer.appendChild(dni[1]);
    formContainer.appendChild(nomActivitat[0]);
    formContainer.appendChild(nomActivitat[1]);

    mostrarBotoEnviar(Constants.POST, Constants.APUNTAR_ACTIVITATS);
}

function envia() {
    const dni = document.getElementById('dni') ? document.getElementById('dni').value : null;
    const nom = document.getElementById('nom') ? document.getElementById('nom').value : null;
    const cognoms = document.getElementById('cognoms') ? document.getElementById('cognoms').value : null;
    const edat = document.getElementById('edat') ? document.getElementById('edat').value : null;
    const contrasenya1 = document.getElementById('contrasenya1') ? document.getElementById('contrasenya1').value : null;
    const contrasenya2 = document.getElementById('contrasenya2') ? document.getElementById('contrasenya2').value : null;
    const nomActivitat = document.getElementById('nomActivitat') ? document.getElementById('nomActivitat').value : null;
    const descripcioActivitat = document.getElementById('descripcioActivitat') ? document.getElementById('descripcioActivitat').value : null;
    const dataActivitat = document.getElementById('dataActivitat') ? document.getElementById('dataActivitat').value : null;
    const boto_accio = document.getElementById('submit').getAttribute('btn_action');
    const boto_tipus = document.getElementById('submit').getAttribute('type_message');

    let url = Constants.URL_APP;

    if (boto_accio === Constants.REGISTRAR_USUARI || boto_accio === Constants.ACTUALITZAR_USUARI || boto_accio === Constants.OBTENIR_INFO_USUARI || boto_accio === Constants.ELIMINAR_USUARI) {
        url += Constants.URL_USUARI;

        if (boto_tipus === Constants.POST || boto_tipus === Constants.PUT) {
            if (!dni || !nom || !cognoms || !edat || !contrasenya1 || !contrasenya2) {
                alert("Hay que rellenar todos los campos");
                return;
            }
            if (contrasenya1 !== contrasenya2) {
                alert("Las contraseñas no coinciden");
                return;
            }
        }

        if (boto_tipus === Constants.DELETE || boto_tipus === Constants.GET) {
            if (!dni) {
                alert("El DNI es obligatorio");
                return;
            }
        }

        if (boto_tipus !== Constants.POST) {
            url += `/${dni}`;
        }
    }

    if (boto_accio === Constants.CREAR_ACTIVITAT || boto_accio === Constants.CONSULTAR_ACTIVITATS || boto_accio === Constants.APUNTAR_ACTIVITATS) {
        url += Constants.URL_ACTIVITAT;
        
        if (boto_accio === Constants.CREAR_ACTIVITAT) {
            if (!nomActivitat || !descripcioActivitat || !dataActivitat) {
                alert("Hay que rellenar todos los campos");
                return;
            }
        } else if (boto_accio === Constants.APUNTAR_ACTIVITATS) {
            if (!nomActivitat || !dni) {
                alert("Hay que rellenar todos los campos");
                return;
            }
            url += `/${Constants.URL_APUNTAR_USUARI}`;
        }

        if (boto_tipus === Constants.DELETE) {
            url += `/${nomActivitat}`;
        }
    }

    const fetchOptions = {
        method: boto_tipus,
        headers: {
            'Content-Type': 'application/json',
        }
    };

    if (boto_tipus !== Constants.GET) {
        const data = {
            dni: dni,
            nom: nom,
            cognoms: cognoms,
            edat: edat,
            contrasenya: contrasenya1,
            nomActivitat: nomActivitat,
            descripcioActivitat: descripcioActivitat,
            dataActivitat: dataActivitat
        };
        fetchOptions.body = JSON.stringify(data);
    }

    fetch(url, fetchOptions)
        .then(response => {
            if (!response.ok) {
                return response.json().then(errData => {
                    throw new Error(errData.message || 'Error en la operación');
                });
            }
            return response.json();
        })
        .then(data => {
            console.log('Success:', data);
            alert("Operación realizada con éxito");
        })
        .catch((error) => {
            console.error('Error:', error);
            alert(error.message || "Error en la operación");
        });
}
