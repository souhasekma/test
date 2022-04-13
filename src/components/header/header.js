import  React from 'react';
import {Navbar, Container, Nav, NavDropdown } from 'react-bootstrap';
import { BsBasket } from 'react-icons/bs';

const header =()=>{
    return(
       <div>
        <Navbar collapseOnSelect expand="lg" bg="danger" variant="dark">
        <Container>
        <Navbar.Brand href="/home">Shop Now </Navbar.Brand>
        <Navbar.Toggle aria-controls="responsive-navbar-nav" />
        <Navbar.Collapse id="responsive-navbar-nav">
          <Nav className="me-auto">
            <NavDropdown title="se connecter" id="collasible-nav-dropdown">
              <NavDropdown.Item href="/connexion">se connecter</NavDropdown.Item>
            </NavDropdown>
            <Nav.Link href="/panier"> <BsBasket/> </Nav.Link>
            
           
          </Nav>
        </Navbar.Collapse>
        </Container>
      </Navbar>
      </div>
    )
  }
  
  export default header;