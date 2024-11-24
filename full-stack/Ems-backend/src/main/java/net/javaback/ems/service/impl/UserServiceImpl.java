package net.javaback.ems.service.impl;

import lombok.AllArgsConstructor;
import net.javaback.ems.dto.UserDto;
import net.javaback.ems.entity.User;
import net.javaback.ems.exception.ResourceNotFoundException;
import net.javaback.ems.mapper.UserMapper;
import net.javaback.ems.repository.UserRepository;
import net.javaback.ems.service.UserService;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.stream.Collectors;

@Service
@AllArgsConstructor




 
public class UserServiceImpl implements UserService {

    private UserRepository userRepository;

    @Override
    public UserDto createUser(UserDto userDto) {

        User user  = UserMapper.mapToUser(userDto);
        User savedUser = userRepository.save(user);

        return UserMapper.mapToUserDto(savedUser);
    }

    @Override
    public UserDto getUserById(Long userId) {
        User user = userRepository.findById(userId)
                .orElseThrow(() -> new ResourceNotFoundException("User is not exists with given id : " + userId));
        return UserMapper.mapToUserDto(user);
    }

    @Override
    public List<UserDto> getAllUsers() {
        List<User> users = userRepository.findAll();
        return users.stream().map((user) -> UserMapper.mapToUserDto(user))
                .collect(Collectors.toList());
    }

    @Override
    public UserDto updateUser(Long userId, UserDto updateUser) {

       User user = userRepository.findById(userId).orElseThrow(
                () -> new ResourceNotFoundException("User is not exists with given id : " + userId)
       );

       user.setLogin(updateUser.getLogin());
        user.setEmail(updateUser.getEmail());
       user.setPassword(updateUser.getPassword());


        User updateUserObg = userRepository.save(user);

        return UserMapper.mapToUserDto(updateUserObg);
    }

    @Override
    public void deleteUser(Long userId) {

        User user = userRepository.findById(userId).orElseThrow(
                () -> new ResourceNotFoundException("User is not exists with given id : " + userId)
        );

        userRepository.delete(user);

    }
}
