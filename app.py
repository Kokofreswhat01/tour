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

    # Ici, vous pouvez traiter les données du formulaire, par exemple, en les enregistrant dans une base de données ou en effectuant des vérifications.

    # Pour l'instant, nous allons simplement renvoyer un message de réussite à l'utilisateur.
    return f'Inscription réussie pour {name}. Votre email est {email}, votre numéro est {numero} et votre mot de passe est {mot_de_passe}.'

if __name__ == '__main__':
    app.run(debug=True)
