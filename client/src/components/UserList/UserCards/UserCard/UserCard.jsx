import React from "react";
import "./UserCard.css";

const UserCard = ({ user_id, username, email, password }) => {

  return (
    <>
        <tr>
          <td className="usersTable-0lax">{user_id}</td>
          <td className="usersTable-0lax">{username}</td>
          <td className="usersTable-0lax">{email}</td>
          <td className="usersTable-0lax">{password}</td>
        </tr>
    </>
  );
};

export default UserCard;
