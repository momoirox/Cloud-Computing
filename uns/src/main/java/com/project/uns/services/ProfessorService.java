package com.project.uns.services;

import java.util.List;

import org.springframework.stereotype.Service;

import com.project.uns.dto.RegisterDto;
import com.project.uns.mapper.Mapper;
import com.project.uns.model.Professor;
import com.project.uns.repository.ProfessorRepository;

import lombok.RequiredArgsConstructor;

@Service
@RequiredArgsConstructor
public class ProfessorService {

  private final ProfessorRepository professorRepository;
  private final Mapper mapper;

  public Professor save(RegisterDto professor) {

    if (!professorRepository.existsByJmbg(professor.getJmbg())) {
      return professorRepository.save(mapper.mapProfessor(professor));
    } else {
      return null;
    }
  }

  public List<Professor> getAll() {
    return professorRepository.findAll();
  }

}
