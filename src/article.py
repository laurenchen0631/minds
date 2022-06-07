from dataclasses import dataclass, asdict


@dataclass
class Article:
    title: str
    subtitle: str
    content: str

    def to_json(self) -> dict[str, str]:
        return asdict(self)

    def to_str(self) -> str:
        return f'{self.title}. {self.subtitle} {self.content}'
