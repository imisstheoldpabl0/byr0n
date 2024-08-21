import React from "react";
import "./UserCard.css";

const UserCard = ({ user_id, username, email, password }) => {
  // importar los datos de la API
  // iterar creando una tarjeta por cada conjunto de datos
  return (
    <section className="userCards">
      <section className="usersTable">
        <table>
          <thead>
            <tr>
              <th>user_id</th>
              <th>username</th>
              <th>email</th>
              <th>password</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>{user_id}</td>
              <td>{username}</td>
              <td>{email}</td>
              <td>{password}</td>
            </tr>
          </tbody>
        </table>
      </section>
    </section>
  );
};

export default UserCard;
