import  React , {Component} from 'react';
import Header from './components/header/header';
import Connexion from './components/connexion/connexion';
import Home from './components/home/home';
import {Routes} from 'react-router-dom';
import {Route} from 'react-router-dom';
import Panier from './components/panier/panier';
import './App.css';
class  App extends Component {
  
  render(){
    return (
      <div className="App">
       <Header /> 
       <Routes>
         <Route path="/home" exact={true}  element={<Home />} />
         <Route path="/connexion"  element={<Connexion />}/>
         <Route path="/panier"  element={<Panier />}/>
        </Routes>
      </div>
  
  );
}
}
export default App;