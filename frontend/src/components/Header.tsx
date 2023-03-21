import {
  Box,
  Button,
  HStack,
  IconButton,
  useDisclosure,
} from "@chakra-ui/react";
import { Link } from "react-router-dom";
import { FaAirbnb, FaMoon } from "react-icons/fa";
import LoginModal from "./LoginModal";

export default function Header() {
  const { onOpen, isOpen, onClose } = useDisclosure();

  return (
    <HStack
      justifyContent={"space-between"}
      py={5}
      px={10}
      borderBottomWidth={1}
    >
      <Box color="red.500">
        <Link to={"/"}>
          <FaAirbnb size={"48"} />
        </Link>
      </Box>
      <HStack spacing={2}>
        <IconButton
          variant={"ghost"}
          aria-label="Toggle dark mode"
          icon={<FaMoon />}
        />
        <Button onClick={onOpen}>Log in</Button>
        <Button colorScheme={"red"}>Sign up</Button>
      </HStack>
      <LoginModal isOpen={isOpen} onClose={onClose} />
    </HStack>
  );
}
