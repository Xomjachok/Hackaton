package net.javaback.ems.service;

import net.javaback.ems.dto.UserDto;

import java.util.List;

public interface UserService {
    UserDto createUser(UserDto userDto);

    UserDto getUserById(Long userId);

    List<UserDto> getAllUsers();

    UserDto updateUser(Long userId, UserDto updateUser);

    void deleteUser(Long userId);
}
