import React from "react";
import "./../../../UserList.css";

const UserTopComp = () => {
  return (
        <thead className="usersTable">
          <tr>
            <th>user_id</th>
            <th>username</th>
            <th>email</th>
            <th>password</th>
          </tr>
        </thead>
  );
};

export default UserTopComp;
