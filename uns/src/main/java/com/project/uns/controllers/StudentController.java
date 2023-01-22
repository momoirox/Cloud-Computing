package com.project.uns.controllers;

import java.util.List;

import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestBody;
import org.springframework.web.bind.annotation.RequestMapping;

import org.springframework.web.bind.annotation.RestController;

import com.project.uns.dto.RegisterDto;
import com.project.uns.model.Student;
import com.project.uns.services.StudentService;

import lombok.RequiredArgsConstructor;

@RestController
@RequestMapping("/students")
@RequiredArgsConstructor
public class StudentController {
    
    private final StudentService studentService;

    @PostMapping
    public  ResponseEntity<RegisterDto> save(@RequestBody RegisterDto  registerDto){
        
        Student student = studentService.save(registerDto);
        if (student != null){
        registerDto.setId(student.getId());
        return new ResponseEntity<>(registerDto, HttpStatus.OK);
     
        }
        return new ResponseEntity<>(registerDto, HttpStatus.CONFLICT);
    }

    @GetMapping
    public List<Student> getAll(){
        return studentService.getAll();
    }
}
