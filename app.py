from flask import Flask, render_template, request

app = Flask(__name__)

# Route pour afficher le formulaire d'inscription
@app.route('/inscription', methods=['GET'])
def show_inscription_form():
    return render_template('inscription.html')

# Route pour traiter les données soumises via le formulaire d'inscription
@app.route('/inscription', methods=['POST'])
def process_inscription_form():
    name = request.form.get('name')
    email = request.form.get('mail')
    numero = request.form.get('numero')
    mot_de_passe = request.form.get('mdp')
    mdp_conf = request.form.get('mdp_conf')

    if mot_de_passe==mdp_conf:
        f'Inscription réussie pour {name}.'
        return render_template('HTML/connexion.html')
    return render_template('HTML/inscription.html') 


@app.route('/connexion', methods=['GET', 'POST'])
def connexion_form():
    email = request.form.get('mail')
    mot_de_passe = request.form.get('mdp')

    if email==email and mot_de_passe==mot_de_passe:
        return render_template('HTML/aceil.html')
    return render_template('HTML/connexion.html')




if __name__ == '__main__':
    app.run(debug=True)
