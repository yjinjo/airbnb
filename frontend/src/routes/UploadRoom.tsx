import ProtectedPage from "../components/ProtectedPage";
import HostOnlyPage from "../components/HostOnlyPage";
import useHostOnlyPage from "../components/HostOnlyPage";

export default function UploadRoom() {
  useHostOnlyPage();
  return (
    <ProtectedPage>
      <h1>Upload roommmmmmmmmm</h1>
    </ProtectedPage>
  );
}
