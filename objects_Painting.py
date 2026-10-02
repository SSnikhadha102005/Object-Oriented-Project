# objects_Painting.py
# Snikhadha Sinha
# 10/01/2026

class Painting:

    def __init__(self, title, medium, hours, minutes, complexity_level):
        self.title = title
        self.medium = medium.lower()
        self.hours = hours
        self.minutes = minutes
        self.complexity_level = complexity_level

    def getTotalMinutes(self):
        """
        Converts hours and minutes to total minutes.
        """
        return (self.hours * 60) + self.minutes

    def estimateDifficulty(self):

        if self.medium in ["pencil", "charcoal"]:
            return "Easy"

        elif self.medium in ["acrylic", "gouache"]:
            return "Medium"

        elif "oil" in self.medium:
            return "Hard"

        elif self.medium in ["watercolor", "ink"]:
            return "Very Hard"

        return "Unknown"

    def isLongProject(self):
        return self.getTotalMinutes() > 180

    def __str__(self):
        return (
            f"Title: {self.title}\n"
            f"Medium: {self.medium}\n"
            f"Duration: {self.getTotalMinutes()} minutes\n"
            f"Complexity: {self.complexity_level}"
        )

    def describePainting(self):
        return (
            f"'{self.title}' was created using {self.medium}. "
            f"It took {self.getTotalMinutes()} minutes to complete "
            f"and has a complexity level of {self.complexity_level}."
        )


# --------------------------------------------------
# PortraitPainting Subclass
# --------------------------------------------------

class PortraitPainting(Painting):

    def __init__(
        self,
        title,
        medium,
        hours,
        minutes,
        complexity_level,
        subject_name
    ):
        super().__init__(
            title,
            medium,
            hours,
            minutes,
            complexity_level
        )

        self.subject_name = subject_name

    def identifySubject(self):
        return self.subject_name

    # Overridden Method
    def describePainting(self):
        return (
            f"'{self.title}' is a portrait painting of "
            f"{self.subject_name}. It was created using "
            f"{self.medium}, took {self.getTotalMinutes()} minutes "
            f"to complete, has a complexity level of "
            f"{self.complexity_level}, is estimated to be "
            f"{self.estimateDifficulty()} in difficulty, "
            f"and qualifies as a long project: "
            f"{self.isLongProject()}."
        )


# --------------------------------------------------
# LandscapePainting Subclass
# --------------------------------------------------

class LandscapePainting(Painting):

    def __init__(
        self,
        title,
        medium,
        hours,
        minutes,
        complexity_level,
        location
    ):
        super().__init__(
            title,
            medium,
            hours,
            minutes,
            complexity_level
        )

        self.location = location

    def describeLocation(self):
        return self.location

    # Overridden Method
    def describePainting(self):
        return (
            f"'{self.title}' is a landscape painting depicting "
            f"{self.location}. It was created using {self.medium}, "
            f"took {self.getTotalMinutes()} minutes to complete, "
            f"has a complexity level of {self.complexity_level}, "
            f"is estimated to be {self.estimateDifficulty()} in "
            f"difficulty, and qualifies as a long project: "
            f"{self.isLongProject()}."
        )


# --------------------------------------------------
# AbstractPainting Subclass
# --------------------------------------------------

class AbstractPainting(Painting):

    def __init__(
        self,
        title,
        medium,
        hours,
        minutes,
        complexity_level,
        theme
    ):
        super().__init__(
            title,
            medium,
            hours,
            minutes,
            complexity_level
        )

        self.theme = theme

    def interpretTheme(self):
        return self.theme

    # Overridden Method
    def describePainting(self):
        return (
            f"'{self.title}' is an abstract painting that explores "
            f"the theme '{self.theme}'. It was created using "
            f"{self.medium}, took {self.getTotalMinutes()} minutes "
            f"to complete, has a complexity level of "
            f"{self.complexity_level}, is estimated to be "
            f"{self.estimateDifficulty()} in difficulty, and "
            f"qualifies as a long project: "
            f"{self.isLongProject()}."
        )