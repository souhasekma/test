import  React from 'react';
import { Button} from 'react-bootstrap';
import {useNavigate} from "react-router-dom";
import { Link } from 'react-router-dom';
function Panier (authorized){
    let navigate = useNavigate();
    return (
        <div>
        <h2>Vos achats</h2> 
        <Link to="/home" className="btn btn-secondary">Continuer mes achats</Link>
        <Link to="/connexion" className="btn btn-secondary">Finaliser votre commande</Link>
        </div>
    )
}
export default Panier ;