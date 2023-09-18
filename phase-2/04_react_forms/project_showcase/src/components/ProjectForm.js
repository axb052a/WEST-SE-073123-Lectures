import { useState } from "react";

const ProjectForm = ({ addProject }) => {
  const [newProject, setNewProject] = useState({
    name: "",
    about: "",
    phase: "",
    link: "",
    image: "",
  });

  const { name, about, phase, link, image } = newProject;

  const handleSubmit = (e) => {
    e.preventDefault();
    const newProject = { name, about, phase, link, image };
    fetch("http://localhost:4000/projects", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(newProject),
    })
      .then((r) => r.json())
      .then((createdProject) => {
        // update state so created project shows up
        setNewProject({
          name: "",
          about: "",
          phase: "",
          link: "",
          image: "",
        });
        addProject(createdProject);
      });
  };

  const handleOnChange = (e) => {
    const key = e.target.name;
    const value = e.target.value;
    setNewProject({ ...newProject, [key]: value });
  };

  return (
    <section>
      <form onSubmit={handleSubmit} className="form" autoComplete="off">
        <h3>Add New Project</h3>

        <label htmlFor="name">Name</label>
        <input
          value={name}
          onChange={handleOnChange}
          type="text"
          id="name"
          name="name"
        />

        <label htmlFor="about">About</label>
        <textarea
          value={about}
          onChange={handleOnChange}
          id="about"
          name="about"
        />

        <label htmlFor="phase">Phase</label>
        <select value={phase} onChange={handleOnChange} name="phase" id="phase">
          <option>Select One</option>
          <option value="1">Phase 1</option>
          <option value="2">Phase 2</option>
          <option value="3">Phase 3</option>
          <option value="4">Phase 4</option>
          <option value="5">Phase 5</option>
        </select>

        <label htmlFor="link">Project Homepage</label>
        <input
          value={link}
          onChange={handleOnChange}
          type="text"
          id="link"
          name="link"
        />

        <label htmlFor="image">Screenshot</label>
        <input
          value={image}
          onChange={handleOnChange}
          type="text"
          id="image"
          name="image"
        />

        <button type="submit">Add Project</button>
      </form>
    </section>
  );
};

export default ProjectForm;

