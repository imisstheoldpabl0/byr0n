import React from "react";
import './UserCard.css'


const UserCard = ({ key, username, email, password, login_status }) => {

  console.log("hello?")

  console.log(`This is UserCard: ${key}, ${username}, ${email}, ${password}, ${login_status}`)

  // importar los datos de la API
  // iterar creando una tarjeta por cada conjunto de datos
  return (
    <section className='userCards'>

      <p>Hello this is userList</p>

      <p>{username}</p>
    </section>
  );
};

export default UserCard;
