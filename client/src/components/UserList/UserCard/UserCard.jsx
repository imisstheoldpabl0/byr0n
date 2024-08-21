import React from "react";
import "./UserCard.css";

const UserCard = ({ username }) => {
  console.log(`This is UserCard: ${username}`);

  // importar los datos de la API
  // iterar creando una tarjeta por cada conjunto de datos
  return (
    <section className="userCards">

      <section className="userCard">
      
        <p>UserCard</p>
        <p>{username}</p>
      
      </section>
    
    </section>
  );
};

export default UserCard;
