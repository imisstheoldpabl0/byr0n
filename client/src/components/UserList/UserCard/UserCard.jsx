import React from "react";
import "./UserCard.css";

const UserCard = ({ user_id, username, email, password }) => {

  return (
    <section className="userCards">
      <section className="usersTable">
        <div id="section-top">
        </div>
        <table>
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
