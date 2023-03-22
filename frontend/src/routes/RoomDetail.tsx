import { useParams } from "react-router-dom";
import { useQuery } from "@tanstack/react-query";
import { getRoom } from "../api";

export default function RoomDetail() {
  const { roomPk } = useParams();
  const { isLoading, data } = useQuery([`rooms`, roomPk], getRoom);
  return <h1>hello</h1>;
}
