import React from "react";
import UserCard from "./UserCard/UserCard";

const UserCards = ({ paintCards }) => {
  return (
    <>
      <tbody className="usersTable">
        {paintCards}
      </tbody>

    </>

  );
};

export default UserCards;
