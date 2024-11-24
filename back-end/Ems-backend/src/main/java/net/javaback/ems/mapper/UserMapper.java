package net.javaback.ems.mapper;

import net.javaback.ems.dto.UserDto;
import net.javaback.ems.entity.User;

public class UserMapper {

    public static UserDto mapToUserDto(User user) {

        return new UserDto(
                user.getId(),
                user.getLogin(),
                user.getEmail(),
                user.getPassword()

        );

    }

    public static User mapToUser(UserDto userDto) {
        return new User(
                userDto.getId(),
                userDto.getLogin(),
                userDto.getEmail(),
                userDto.getPassword()

        );
    }

}
