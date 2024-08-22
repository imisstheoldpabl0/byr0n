import React from "react";
import "./UserTopComp.css";

const UserTopComp = () => {
  return (
        <thead className="top-row">
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
