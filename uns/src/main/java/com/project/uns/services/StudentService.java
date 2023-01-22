package com.project.uns.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.project.uns.dto.RegisterDto;
import com.project.uns.mapper.Mapper;
import com.project.uns.model.Student;
import com.project.uns.repository.StudentRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class StudentService {

  private final StudentRepository studentRepository;
  private final Mapper mapper;

  public Student save(RegisterDto student) {
    
    if (!studentRepository.existsByJmbg(student.getJmbg())) {
      return studentRepository.save(mapper.mapStudent(student));
    } else {
      return null;
    }

  }

  public List<Student> getAll() {
    return studentRepository.findAll();
  }

}
